from abc import ABC, abstractmethod

class CourseManager(ABC):
    @abstractmethod
    def create_course(self, course_id:str, course_name:str, course_description:str):
        pass

    @abstractmethod
    def delete_course(self, course_id:str):
        pass

class UserManager(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def remove_user(self, user):
        pass