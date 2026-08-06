from threading import Thread

import app
import webhook


def run_bot():
    app.main()


def run_webhook():
    webhook.app.run(
        host="0.0.0.0",
        port=5000
    )


if __name__ == "__main__":

    Thread(
        target=run_webhook,
        daemon=True
    ).start()

    run_bot()
