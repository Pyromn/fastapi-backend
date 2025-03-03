
import asyncio

from prisma import Prisma

async def main() -> None:
   db = Prisma(auto_register=True)
   await db.connect()

   users = await db.user.find_many()

   print(users)

   users = await db.user.find_many(
       include={
           'Posts': True,
       },
   )

   print(users)

   posts = await db.post.find_many(
       include={
           'User': True,
       },
   )

   print(posts)

   posts = await db.post.find_many(
       where={
           'OR': [
               {'title': {'contains': 'prisma'}},
           ]
       }
   )

   print(posts)

   await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())