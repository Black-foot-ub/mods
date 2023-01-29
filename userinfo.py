from pyrogram import Client, types
from blackfoot import loader, utils  # type: ignore


class UserInfoMod(loader.Module):
    """Get info about user"""

    strings = {
        "name": "UserInfo",
        "no_reply": "<b>🚫 Reply to message!</b>",
        "channel_info": (
            "<b>ID: {}" "\nTitle: {}" "\nDescription: {}" "\nMembers: {}</b>"
        ),
        "user_info": (
            "<b>ID: {}"
            "\nFIrst name: {}"
            "\nLast name: {}"
            "\nUsername: {}"
        ),
    }

    async def userinfocmd(self, client: Client, message: types.Message):
        """Get user info. Usage: .userinfo [reply]"""

        reply = message.reply_to_message

        if not reply:
            await utils.answer(message, self.strings["no_reply"])
            return

        if reply.sender_chat:
            sender = reply.sender_chat
            await utils.answer(
                message,
                self.strings["channel_info"].format(
                    sender.id,
                    utils.escape_html(sender.title),
                    utils.escape_html(sender.description),
                    sender.members_count,
                ),
            )
            return
        else:
            sender = reply.from_user
            await utils.answer(
                message,
                self.strings["user_info"].format(
                    sender.id,
                    utils.escape_html(sender.first_name),
                    utils.escape_html(sender.last_name),
                    sender.username,
                ),
            )
            return
