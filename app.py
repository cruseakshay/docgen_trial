import json
import requests
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)
TOKEN = "Your API TOKEN from BotFather"


def imageAsDict(imageURL, caption):
    """
    Creates a dictionary representation of an image with its URL and caption.

    Args:
        imageURL (str): The URL of the image.
        caption (str): The caption for the image.

    Returns:
        dict: A dictionary representing the image with its URL and caption.
    """
    return {
        "type": "photo",
        "media": imageURL,
        "caption": caption,
    }


def sendMediaGroup(chatid, allImages):
    """
    Sends a group of media (images) to a Telegram chat.

    Args:
        chatid (int): The ID of the chat where the media will be sent.
        allImages (list): A list of dictionaries containing the source URL and prompt for each image.

    Returns:
        requests.Response: The response object from the API call.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMediaGroup"
    media = [imageAsDict(allImages[i]["src"], allImages[i]["prompt"]) for i in range(5)]
    payload = {"chat_id": chatid, "media": media}
    r = requests.post(url, json=payload)
    return r


def sendMessage(chat_id, text):
    """
    Sends a text message to a Telegram chat.

    Args:
        chat_id (int): The ID of the chat where the message will be sent.
        text (str): The text of the message.

    Returns:
        requests.Response: The response object from the API call.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    r = requests.post(url, json=payload)
    return r


@app.post("/")
def index():
    """
    Handles the index route of the web app.

    Returns:
        Response: A response object with a status code of 200 indicating a successful request.
    """
    msg = request.get_json()
    chat_id = msg["message"]["chat"]["id"]
    inputText = msg["message"]["text"]
    if inputText == "/start":
        sendMessage(chat_id, "Ya, I am Online. Send me a Prompt")
    else:
        BASE_URL = "https://lexica.art/api/v1/search?q=" + str(inputText)
        response = requests.get(BASE_URL)
        response_text = json.loads(response.text)
        allImages = response_text["images"]
        sendMediaGroup(chat_id, allImages)
    return Response("ok", status=200)
