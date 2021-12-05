from src.signalbot import Command, Context


class FridayCommand(Command):
    def describe(self) -> str:
        return "🦀 Congratulations sailor, you made it to friday!"

    async def handle(self, c: Context):
        command = c.message.text

        if command == "friday":
            image = "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"
            await c.send(
                "https://www.youtube.com/watch?v=pU2SdH1HBuk",
                base64_attachments=[image],
            )
            return
