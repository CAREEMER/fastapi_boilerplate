Sample project

## Make migrations
`alembic revision --autogenerate -m "init"`

## Upgrade migrations to head
`alembic upgrade head`

## Downgrade migrations
`alembic downgrade -1`
