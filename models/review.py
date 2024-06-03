#!/usr/bin/python3
"""define the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represent a review

    Attributes:
        place_id (str): = place id
        user_id (str): = user id
        text (str): = the text of the review
    """
    def __init__(self, kwargs):
        super().__init__(**kwargs)
        if "place_id" not in kwargs:
            self.place_id = ""
        if "user_id" not in kwargs:
            self.user_id = ""
        if "text" not in kwargs:
            self.text = ""

# Example usage
if __name__ == "__main__":
    review = Review(place_id="12345", user_id="67890", text="Great place!")
    print(review.place_id)  # Should output: 12345
    print(review.user_id)   # Should output: 67890
    print(review.text)      # Should output: Great place!
