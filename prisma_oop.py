
import asyncio

from prisma import Prisma

from prisma.models import User

async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()


    users = await User.prisma().find_many()

    # print(users)

    for user in users:
        print(user.id)
        print(user.name)
        print(user.email)


    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())