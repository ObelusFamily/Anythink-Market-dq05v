import pytest
from unittest.mock import MagicMock
from typing import List, Optional

# from app.db.repositories.items import ItemsRepository
import app.api.routes.comments
from app.models.domain.items import Item
from app.models.domain.comments import Comment
from app.models.domain.users import User

from app.models.domain.profiles import Profile

from app.models.schemas.comments import (
    CommentInCreate,
    CommentInResponse,
    ListOfCommentsInResponse,
)

class FakeRepo():
    def __init__(self):
        self.__comment_list = ListOfCommentsInResponse(comments=[])
    async def get_comments_for_item(
        self,
        *,
        item: Item,
        user: Optional[User] = None,
    ) -> List[Comment]:
        return self.__comment_list.comments

    async def create_comment_for_item(
        self,
        *,
        body: str,
        item: Item,
        user: User,
    ) -> Comment:
        profile = Profile(username=user.username, email=user.email)
        comment = Comment(body=body, seller=profile)
        self.__comment_list.comments.append(comment)
        return comment

def test_mytest():
    assert 1 == 1

async def test_empty_repo():
    repo = FakeRepo()
    user = User(username='user', email='user@place.com')
    comments_list = await app.api.routes.comments.list_comments_for_item(
        'foo', user, repo)
    assert len(comments_list.comments) == 0

async def test_one_comment():
    repo = FakeRepo()
    user = User(username='user', email='user@place.com')
    await app.api.routes.comments.create_comment_for_item(
        CommentInCreate(body='body'), 'foo', user, repo)

    comments_list = await app.api.routes.comments.list_comments_for_item(
        'foo', user, repo)
    print(comments_list.comments)
    assert len(comments_list.comments) == 1

async def test_one_comment2():
    repo = FakeRepo()
    user = User(username='user', email='user@place.com')
    await app.api.routes.comments.create_comment_for_item(
        CommentInCreate(body='body2'), 'foo2', user, repo)

    comments_list = await app.api.routes.comments.list_comments_for_item(
        'foo', user, repo)
    print(comments_list.comments)
    assert len(comments_list.comments) == 1

async def test_one_comment3():
    repo = FakeRepo()
    
    user = User(username='user', email='user@place.com')
    await app.api.routes.comments.create_comment_for_item(
        CommentInCreate(body='body3'), 'foo3', user, repo)

    comments_list = await app.api.routes.comments.list_comments_for_item(
        'foo', user, repo)
    print(comments_list.comments)
    assert len(comments_list.comments) == 1
