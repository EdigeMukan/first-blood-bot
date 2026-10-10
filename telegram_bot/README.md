# Telegram-бот на aiogram

Простой Telegram-бот на aiogram 3: команды `/start` и `/help`, ответы на текстовые сообщения и подсказка для неподдерживаемых сообщений.

## Запуск в Replit

1. Создайте бота через [@BotFather](https://t.me/BotFather) и скопируйте выданный токен.
2. Откройте **Tools → Secrets** в Replit и добавьте секрет `TELEGRAM_BOT_TOKEN`.
3. Запустите workflow **Telegram Bot**.

Токен не нужно вставлять в исходный код или коммитить в репозиторий.

## Локальный запуск

Установите зависимости из корня проекта:

```bash
python -m pip install "aiogram>=3.31.0,<4.0"
```

Перед запуском задайте переменную окружения `TELEGRAM_BOT_TOKEN`, затем из корня проекта выполните:

```bash
python -m telegram_bot.main
```

Бот использует long polling и не требует публичного HTTP-сервера.
