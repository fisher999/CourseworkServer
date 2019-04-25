from booking.models import Feedback
from booking.models import Hotel
from django.conf import settings
from django.utils import timezone
import json


class FeedbackManager:
    @staticmethod
    def getFeedbacks(hotel_id, currentUser):
        feedbacks = Feedback.objects.filter(hotel__id=hotel_id)
        feedbacksDictArr = []
        for feedback in feedbacks:
            feedbackDict = {}
            feedbackDict['id'] = feedback.id
            user = feedback.user
            userDict = {}
            userDict['id'] = user.id
            userDict['username'] = user.username
            if currentUser.id == user.id:
                userDict['isMyComment'] = True
            else:
                userDict['isMyComment'] = False
            feedbackDict['user'] = userDict
            feedbackDict['rating'] = feedback.rating
            feedbackDict['date'] = feedback.date.strftime('%d-%m-%Y %H:%M')
            feedbackDict['comment'] = feedback.comment
            feedbacksDictArr.append(feedbackDict)

        jsonObject = json.dumps(feedbacksDictArr).encode('utf8')

        return jsonObject

    @staticmethod
    def postFeedback(user, hotel_id, args):
        hotel = Hotel.objects.get(id=hotel_id)
        rating = args['rating']
        comment = args['comment']
        date = timezone.now()

        feedback = Feedback(hotel=hotel, user=user, rating=rating, comment=comment, date=date)
        feedback.save()

        feedbackDict = {}
        feedbackDict['id'] = feedback.id
        user = feedback.user
        userDict = {}
        userDict['id'] = user.id
        userDict['username'] = user.username
        feedbackDict['user'] = userDict
        feedbackDict['rating'] = feedback.rating
        feedbackDict['date'] = feedback.date.strftime('%d-%m-%Y %H:%M')
        feedbackDict['comment'] = feedback.comment

        jsonObject = json.dumps(feedbackDict).encode('utf8')

        return jsonObject

    @staticmethod
    def deleteFeedback(user, feedback_id):
        feedbacks = Feedback.objects.filter(user__id=user.id)
        for feedback in feedbacks:
            if feedback.id == feedback_id:
                feedback.delete()
                response = {}
                response['success'] = True
                response['message'] = 'Feedback deleted!'
                json_object = json.dumps(response).encode('utf8')
                return json_object

        response = {}
        response['success'] = False
        response['message'] = 'Feedback not deleted! (Its not exist!)'
        json_object = json.dumps(response).encode('utf8')
        
        return json_object





