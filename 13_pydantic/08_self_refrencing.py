from typing import List,Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id:int
    description:str
    replies:Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(
    id=12,
    description="comment 1",
    replies=[
        Comment(
            id=34,
            description="nested comment 1"
        ),
        Comment(
            id=44,
            description="nested comment 2"
        ),
        Comment(
            id=54,
            description="nested comment 3",
            replies=[
                Comment(
                    id=55,
                    description="nested nested comment"
                )
            ]
        ),
    ]
)

print(comment)