from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    await message.answer(
        "Привет! Я твой личный бот, и скоро мы вместе поступим в Стэнфорд! "
        "🎓 Напиши мне что-нибудь!"
    )


@router.message(Command("help"))
async def handle_help(message: Message) -> None:
    await message.answer(
        "Доступные команды:\n"
        "/start — начать работу\n"
        "/help — показать эту справку\n\n"
        "Также отправь любое текстовое сообщение, чтобы получить ответ."
    )


@router.message(F.text.startswith("/"))
async def handle_unknown_command(message: Message) -> None:
    await message.answer("Не знаю эту команду. Используй /help.")


@router.message(F.text)
async def handle_text(message: Message) -> None:
    if message.text is not None:
        if "что ты умеешь для меня" in message.text.casefold():
            await message.answer("ради тебя на все")
            return
        if "универ" in message.text.casefold():
            await message.answer(
                "Твоя цель — США! Стэнфорд, Беркли и Wharton ждут тебя. "
                "Главное — не бросай кодить! 🇺🇸"
            )
            return
        await message.answer(f"Ты написал(а): {message.text}")


@router.message()
async def handle_unsupported_message(message: Message) -> None:
    await message.answer("Пока я умею отвечать только на текстовые сообщения.")
