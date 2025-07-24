#importing required libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint # type: ignore
from tensorflow.keras.applications import VGG16 # type: ignore
import matplotlib.pyplot as plt

# constants
IMAGE_SIZE = (256, 256)
BATCH_SIZE = 32
EPOCHS = 50
NUM_CLASSES = 2  # Healthy vs Diseased (for crops)
ANIMAL_CLASSES = 3  # Dog, Cat, Human (for filtering)

# paths
DATASET_DIR = 'ML/dataset'
MODEL_DIR = 'agri_model.h5'

def create_model(input_shape, num_classes):
    # create a cnn model for classification
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(256, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy',  # <-- change here
        metrics=['accuracy']
    )
    return model


def train_crop_model():
    # Data generators with augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2
    )

    # Load datasets
    train_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "crops"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )
    
    # Create and train the model
    model = create_model((IMAGE_SIZE[0], IMAGE_SIZE[1], 3), NUM_CLASSES)
    
    callbacks = [
        ModelCheckpoint(MODEL_DIR, save_best_only=True),
        EarlyStopping(patience=5, restore_best_weights=True)
    ]
    
    history = model.fit(
        train_generator,
        steps_per_epoch = train_generator.samples // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE,
        callbacks=callbacks
    )
    
    # plot training history
    plot_training_history(history)
    return model

def train_animal_filter():
    # secondary model to filter out animals/humans
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    train_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )
    validation_generator = train_datagen.flow_from_directory(
        os.path.join(DATASET_DIR, "animals"),
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )
    
    model = create_model(IMAGE_SIZE + (3,), ANIMAL_CLASSES)
    
    model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // BATCH_SIZE,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // BATCH_SIZE,
    )
    
    return model

def plot_training_history(history):
    # Plot training and validation accuracy/loss
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')

    plt.savefig('training_history.png')
    plt.close()
    
def predict_image(model,animal_model, image_path):
    #  predict if image is healthy or diseased
    img = keras.preprocessing.image.load_img(image_path, target_size=IMAGE_SIZE)
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    # check if animal/human
    animal_prediction = animal_model.predict(img_array)
    animal_classes = ['Dog', 'Cat', 'Human']
    animal_prob = np.max(animal_prediction)
    
    if animal_prob > 0.9:
        return {
            type: 'animal',
            'class': animal_classes[np.argmax(animal_prediction)],
            'confidence': float(animal_prob)
        }
        
    # if not animal, check for crops
    crop_prediction = model.predict(img_array)
    crop_classes = ['Healthy', 'Diseased']
    return {
        'type': 'crop',
        'class': crop_classes[np.argmax(crop_prediction)],
        'confidence': float(np.max(crop_prediction))
    }
    
if __name__ == "__main__":
    # train or load models
    if not os.path.exists(MODEL_DIR):
        crop_model = train_crop_model()
        animal_filter_model = train_animal_filter()
    else:
        crop_model = tf.keras.models.load_model(MODEL_DIR)
        animal_filter_model = create_model(IMAGE_SIZE + (3,), ANIMAL_CLASSES)
        
    # test prediction
    test_image_path = "ML/test_image.jpg"  
    if os.path.exists(test_image_path):
        result = predict_image(crop_model, animal_filter_model, test_image_path)
        print(f"Prediction Result: {result}")
        print(f"Type: {result['type']}")
        print(f"Class: {result['class']}")
        print(f"Confidence: {result['confidence']:.2%}")
    else:
        print(f"Test image not found at {test_image_path}. Please provide a valid image path.")