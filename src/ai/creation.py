```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class AIAgent:
    def __init__(self, user_preferences):
        self.user_preferences = user_preferences
        self.model = self.create_model()

    def create_model(self):
        model = keras.Sequential()
        # Customize the model based on user preferences
        for layer_config in self.user_preferences['layers']:
            model.add(layers.Dense(layer_config['units'], activation=layer_config['activation']))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, data, labels):
        self.model.fit(data, labels, epochs=self.user_preferences['epochs'])

    def predict(self, data):
        return self.model.predict(data)

def create_ai_agent(user_preferences):
    ai_agent = AIAgent(user_preferences)
    return ai_agent
```