import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import openai

openai.api_key = "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"

class ChatbotApp(App):
    def build(self):



        # Create the main layout
        layout = BoxLayout(orientation="vertical")
        # Create the headline label and add it to the layout
        headline = Label(text="Welcome to Jarvis", font_size=24, size_hint=(1, 0.1))
        layout.add_widget(headline)

        # Create the chat history label and add it to the layout
        self.history = Label(text="", font_size=14)
        layout.add_widget(self.history)

        # Create the input field and the send button
        input_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=50)
        self.input = TextInput(multiline=False, size_hint=(0.7, None), height=50)
        send_button = Button(text="Send", size_hint=(0.3, None), height=50)
        send_button.bind(on_press=self.send_message)

        # Add the input field and the send button to the input layout
        input_layout.add_widget(self.input)
        input_layout.add_widget(send_button)

        # Add the input layout to the main layout
        layout.add_widget(input_layout)



        return layout

    def send_message(self, instance):
        # Get the user's message from the input field
        message = self.input.text


        # Add the user's message to the chat history
        self.history.text += "\n\nYou: " + message

        # Generate a response to the user's message using GPT-3
        response = openai.Completion.create(
            engine="davinci",
            prompt=message,
            max_tokens=600,
            n=2,
            stop=None,
            temperature=0.7
        )

        # Add the response to the chat history, splitting it into multiple lines if necessary
        response_lines = response.choices[0].text.split("\n")
        formatted_response = "\n \nChatbot: "
        line_length = 0
        for line in response_lines:
            if len(line) + line_length > 60:
                formatted_response += "\n" + line
                line_length = len(line)
            else:
                formatted_response += line
                line_length += len(line)
        self.history.text += formatted_response

        # Clear the input field
        self.input.text = ""


if __name__ == '__main__':
    ChatbotApp().run()