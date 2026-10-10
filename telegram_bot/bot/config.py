from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    bot_token: str

    @classmethod
    def from_env(cls) -> "Settings":
        token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        if not token:
            raise RuntimeError(
                "Не задан TELEGRAM_BOT_TOKEN. Добавьте токен бота в Secrets Replit."
            )
        return cls(bot_token=token)
