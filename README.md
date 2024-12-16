# whats the point of this library?

Graba help you to write better tests mixing concepts like "property testing" and "faker" ideas.

This library help you to make clear the concept of a test, but also it help you to explain/document some of your domain concepts.

As an example, a traditional test might look like this:



```python
def test_user_can_delete_post():
  user = User(
    id=11,
    firstname="John",
    email="anemail@gmail.com",
    mobile="666777888"
    role="admin",
    city="NY",
    enable=True,
    department= "management"
  )
  
  post = Post(
    id=22,
    owner=user,
    content="this is the content of my post"
    showed=True
  )
  
  service_post.delete(post)
  
  assert None == service_post.find_post(id=22)
```

Is a simple example, but you might wonder: 

 - is it relevant in the test that mobile?
 - is it relatevant if the user is enabled or the post is now showed?
 - for this test can I create a user with a different role?
 - is it good this combination of values?. For example even if the test pass, in our company an admin user works in the administration department, however this test is very loose, and is passing using department="management"



Graba reduce all this "specification noise", so you focus on the properties that really matter. So this test would look like this:

```python
from graba.main import Any

def test_user_can_delete_post():
  user = User(
    id=         Any.positiveNumber(),
    firstname=  Any.word(),
    email=      Any.email(),
    mobile=     Any.mobile()
    role=       Any.of(["admin", "user"]),
    city=       Any.word(),
    enable=     True,
    department= Any.of([None, "administration", "management"])
  )
  
  post = Post(
    id=         Any.positiveNumber(),
    owner=      user,
    content=    Any.sentence()
    showed=     Any.boolean()
  )
  
  service_post.delete(post)
  
  assert None == service_post.find_post(id=post.id)
```

This makes clear a few things:

-that the user must be enabled, but also that the role can be multiple, not just "admin" as we specified before.

-it doesnt matter if the post is showed or not



Now we are more clear about our tests values of interests. However still we can missconfigure the initialization of our objects. So lets give an step further

----

# How can you leavarage the most of this library?

This library "shines" when is combined with "builder" pattern, for multiple reasons.

As an example of this:

```python
from app.infrastructure.orm.OrmUser import OrmUser, EnumUserSessionmethod, EnumUserRole
from tests.Any import Any


class BuilderUser:

    def __init__(self):
      	self.id=Any.positiveNumber()
        self.email=Any.email()
        self.created_at=Any.dateTime()
        self.email=Any.email()
        self.email_confirmed=Any.bool()
        self.role=Any.of(["admin", "user", "manager"])
        self.department=Any.of([None, "management", "administration"])
        
    def build(self)->User:
        return User(
            id=self.id,
            email=self.email,
            created_at=self.created_at,
            email_confirmed=self.email_confirmed,
            role=self.role,
            department=self.department
        )

    def admin(self):
      	# now you can see how builder explain different types of initializing things in your applications
        # in this case, we explain that an admin is using admin role, but also is working in administration department
        self.role="admin"
        self.department = "administration"
        return self

    def user(self):
        self.role="user"
        self.department = None
        return self

    def manager(self):
        self.role="manager"
        self.department = "management"
        return self

    def withEmail(self, email):
        self.email=email
        return self

    def withCreatedAt(self, created_at):
        self.created_at=created_at
        return self

    def withEmailConfirmed(self):
        self.email_confirmed = True
        return self

    def withEmailNotConfirmed(self):
        self.email_confirmed = False
        return self
      
class BuilderPost:

    def __init__(self):
        self.id=Any.email()
        self.owner=BuilderUser().build()
        self.content=Any.sentene()
        self.showed=Any.bool()
        
    def with_owner(self, owner: User):
      self.owner= user
      return self
```

Then in your tests you use this builder like:

```python
from graba.main import Any

def test_user_can_delete_post():
  user = BuilderUser()\
            .admin()\
            .withCreatedAt(Any.dateTimeAfter(datetime(2024, 12, 16, 14, 30, 0)))\
            .build()
  
  post = BuilderPost()\
            .withOwner(user)\
            .build()
  
  service_post.delete(post)
  
  assert None == service_post.find_post(id=post.id)
```

