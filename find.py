
import asyncio

from prisma import Prisma

async def main() -> None:
   db = Prisma(auto_register=True)
   await db.connect()

   users = await db.user.find_many()

   users = await db.user.find_many(
       include={
           'posts': True,
       },
   )

   posts = await db.post.find_many(
       where={
           'OR': [
               {'title': {'contains': 'prisma'}},
               {'content': {'contains': 'prisma'}},
           ]
       }
   )

   await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())