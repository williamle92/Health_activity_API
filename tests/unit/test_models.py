from models.activitylog import ActivityLog
from models.healthlog import HealthLogModel
from models.user import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new user is created
    THEN check the email and password are defined correctly
    """
    test_user = User('test1234224', "test1211034@gmail.com", "test12345")
    test_healthlog = HealthLogModel(200, "test1234224")
    test_activity = ActivityLog('test1234224', "run", "Excellent", 60, "test run great")
    test_user.healthlogs.append(test_healthlog)
    test_user.activitylogs.append(test_activity)

    assert test_user.username != "test1234"
    assert test_user.email == "test1211034@gmail.com"
    assert test_healthlog.user_username == "test1234224"
    assert test_activity.user_username != "test1234"



