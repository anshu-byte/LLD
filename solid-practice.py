# Single Responsiblity Principle
# A class should have a single responsibility


# Wrong way
class UserManager:
    def authenticate_user(self, user_name, password):
        pass

    def update_user_profile(self, user_id, new_profile):
        pass

    def send_email_notification(self, user_email, message):
        pass


# Right way


class UserAuthenticator:
    def authenticate_user(self, user_name, password):
        pass


class UserProfileManager:
    def update_user_profile(self, user_id, new_profile):
        pass


class EmailNotifier:
    def send_email_notification(self, user_email, message):
        pass


# Open/Closed Principle
# Classes should be open for extension, but closed for modification

# Wrong way


class ShapeCalculator:
    def calculate_area(self, shape):
        if shape == "square":
            pass
        elif shape == "rectangle":
            pass
        elif shape == "circle":
            pass

    def calculate_perimeter(self, shape):
        if shape == "square":
            pass
        elif shape == "rectangle":
            pass
        elif shape == "circle":
            pass


# Right way

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Liskov Substitution Principle
# If S is a subtype of T, then objects of type T in a program may be replaced with objects of type
# S without altering any of the desirable properties of that program.


# Wrong way


class Vehicle:
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        pass


class Bicycle(Vehicle):
    def start_engine(self):
        pass


# Right way


class Vehicle:
    def start(self):
        raise NotImplementedError


class Car(Vehicle):
    def start(self):
        pass


class Bicycle(Vehicle):
    def start(self):
        pass


# Interface Segregation Principle
# Clients should not be forced to depend on methods that they do not use.

# Wrong way


class MediaPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def play_video(self, video_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError

    def stop_video(self):
        raise NotImplementedError

    def adjust_audio_volume(self, volume):
        raise NotImplementedError

    def adjust_video_brightness(self, brightness):
        raise NotImplementedError


# Right way


class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError

    def adjust_audio_volume(self, volume):
        raise NotImplementedError


class VideoPlayer:
    def play_video(self, video_file):
        raise NotImplementedError

    def stop_video(self):
        raise NotImplementedError

    def adjust_video_brightness(self, brightness):
        raise NotImplementedError


class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        pass

    def stop_audio(self):
        pass

    def adjust_audio_volume(self, volume):
        pass


class AviVideoPlayer(VideoPlayer):
    def play_video(self, video_file):
        pass

    def stop_video(self):
        pass

    def adjust_video_brightness(self, brightness):
        pass


# Dependency Inversion Principle
# High-level modules should not depend on low-level modules; both should depend on abstractions.


# Wrong way
class GmailClient:  # low level module
    def send_email(self, recipient, subject, body):
        pass


class EmailService:  # high level module
    def __init__(self):
        self.gmail_client = GmailClient()

    def send_email(self, recipient, subject, body):
        self.gmail_client.send_email(recipient, subject, body)
