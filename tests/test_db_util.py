import psycopg2

from db_util import DBUtil
from models.profile import Profile


def run():
    util = DBUtil()

    prof = Profile(
        profileUsername="test", profilePasswordHash="naosethunsaoteuh",
        profilePoints=54, profileEmail="test@example.com",
        profileTotalPoints=500, profileToken="snotheusatnusaoh",
        profileName="Testko", profileSurname="Testi"
    )



    try:
        util.insert(prof)
        util.insert(prof)
    except psycopg2.errors.UniqueViolation:
        util.rollback()
        print("Duplication protection works!")

    prof.profilePoints += 1000

    util.update(prof, profileUsername=prof.profileUsername)

    new_prof = util.filter(Profile, profileUsername="test")[0]

    print(new_prof)

    print(util.filter(Profile))

    util.delete(new_prof)
