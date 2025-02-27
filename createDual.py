
import asyncio

from prisma import Prisma

async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()

    user = await db.user.create(
        data={
            'name': 'Robert',
            'email': 'robert@craigie.dev',
            'posts': {
                'create': {
                    'title': 'My first post from Prisma!',
                },
            },
        },
    )

    post = await db.post.update(
        where={
            'id': 42,
        },
        data={
            'authorId': {
                'increment': 1,
            },
        },
    )

    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())