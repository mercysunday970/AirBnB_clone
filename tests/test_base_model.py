#!/usr/bin/python3
import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):

    """
    Unit test for the class BaseModel
    """
    def test_init(self):

        """
        Unit test for the instantiation
        of the BaseModel class
        """
        # to test if a BaseModel is initiated
        user = base_model.BaseModel()
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "id"))
        self.assertIsNotNone(user)
        self.assertIsInstance(user, BaseModel)
        user_dict = user.to_dict()

        # to test if a BaseModel is initiated using kwargs
        my_new_user = base_model.BaseModel(**user_dict)
        self.assertTrue(hasattr(my_new_user, "created_at"))
        self.assertTrue(hasattr(my_new_user, "updated_at"))
        self.assertTrue(hasattr(my_new_user, "id"))
        self.assertIsNotNone(user)
        self.assertIsInstance(user, BaseModel)

    def test_save(self):
        """
        unit test for the save method of
        the BaseModel class
        """
        user = base_model.BaseModel()
        user.updated_at = datetime(2018, 2, 28, 2, 6, 55,  258896)
        date1 = user.updated_at
        user.save()
        date2 = user.updated_at
        self.assertNotEqual(date1, date2)

    def test_to_dict(self):
        """
        Unit test for the to_dict method of
        the BaseModel class
        """
        user = BaseModel()
        value_id = user.id
        value_created_at = user.created_at.isoformat()
        value_updated_at = user.updated_at.isoformat()
        value_class = user.__class__.__name__
        mydict ={'id': value_id, 'created_at': value_created_at, 'updated_at': value_updated_at, '__class__': value_class}
        actual_dict = user.to_dict()
        self.assertDictEqual(actual_dict, mydict)

if __name__ == "__main__":
    unittest.main()
