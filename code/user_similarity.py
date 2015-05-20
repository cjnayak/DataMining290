from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import itertools

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches,
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/

    def user_business(self, _,record):
        if record['type'] == 'review':
            yield[record['user_id'], record['business_id']]

    def businessuser_set(self, user_id, business_ids):
        yield[user_id, list(business_ids)]

        #print user_id, list(business_ids)

    def all_users(self,user_id,business):
        yield["USERKEY", [user_id, business]]
        #print "USERKEY"

## Jaccard Similarity = A U B / A
##http://docs.python.org/2/library/itertools.html
    def jaccard(self, USERKEY, business):
        combos = list(itertools.combinations(list(business),2))
        #print combos
        for c in combos:
                a = set(c[0][1])
                b = set(c[1][1])
                #print 'combos'
                #print a
                #print b
                user_id_1 = c[0][0]
                user_id_2 = c[1][0]
                #print user_id_1
                #print user_id_2
                jaccard = (float(len(a&b)))/(float(len(a|b)))
                #print jaccard
                if jaccard >= 0.50:
                        yield [str(user_id_1), str(user_id_2)],jaccard

    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [self.mr(self.user_business, self.businessuser_set),
                self.mr(self.all_users, self.jaccard)]


if __name__ == '__main__':
    UserSimilarity.run()
