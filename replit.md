# Telegram Bot on aiogram

A starter Telegram bot built with aiogram 3, with `/start`, `/help`, text replies, and secure token configuration.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `python -m telegram_bot.main` — run the Telegram bot
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required secret: `TELEGRAM_BOT_TOKEN` — create a bot with @BotFather and add its token in Replit Secrets

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- Python 3.12, aiogram 3
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `telegram_bot/` — Python Telegram bot, handlers, configuration, and setup guide
- `artifacts/api-server/` — shared Express API server
- `artifacts/mockup-sandbox/` — design canvas preview server

## Architecture decisions

- The Telegram bot uses long polling, so it does not require an HTTP port or webhook.
- The bot token is read from the `TELEGRAM_BOT_TOKEN` environment variable and must be stored as a Replit Secret.

## Product

- Responds to `/start` and `/help`, echoes text, and explains when it receives an unsupported message.

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

_Populate as you build — sharp edges, "always run X before Y" rules._

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
