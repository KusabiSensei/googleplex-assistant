def request_rejected():
    return {
        "payload": {
            "google": {
                "expectUserResponse": False,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": "Oops. Googleplex Assistant says the right token isn't configured.",
                                "displayText": "Oops. Googleplex Assistant says the right token isn't configured."
                            }
                        }
                    ]
                }
            }
        }
    }


def request_accepted():
    return {
        "payload": {
            "google": {
                "expectUserResponse": False,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": "Got it. Playing the requested media.",
                                "displayText": "Got it. Playing the requested media."
                            }
                        }
                    ]
                }
            }
        }
    }