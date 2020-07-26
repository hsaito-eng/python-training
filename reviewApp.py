# 映画、小説等のレビューを登録・参照するアプリ

class Review:
    review_count = 0
    posts = []
    
    @classmethod
    def get_review_count(cls):
        return cls.review_count

    @classmethod
    def show_review(cls):
        for (number, post) in enumerate(cls.posts):
            print("[" + str(number) + "]：" + post["title"] + "のレビュー")

        while True:   
            try:
                user_input = input("見たいレビューの番号を入力してください：\n")
                post = {}
                post = cls.posts[int(user_input)]
                
            except:
                print("入力された値は無効な値です")
            
            else:
                line = "\n---------------------------"
                print("ジャンル : " + post["genre"] + line)
                print("タイトル : " + post["title"] + line)
                print("感想 :" + "\n" + post["impression"] + line)
                break
    
    def __init__(self):
        post = {}
        self.genre = input("ジャンルを入力してください:\n")
        self.title = input("タイトルを入力してください:\n")
        self.impression = input("感想を入力してください:\n")
        post["genre"] = self.genre
        post["title"] = self.title
        post["impression"] = self.impression
        Review.posts.append(post)
        Review.review_count += 1
        
while True:
    print("レビュー数：" + str(Review.get_review_count()))
    print("[0]レビューを書く")
    print("[1]レビューを読む")
    print("[2]アプリを終了する")
    user_input = int(input())
    if user_input == 0:
        review = Review()
    elif user_input == 1:
        Review.show_review()
    elif user_input == 2:
        exit()
    else:
        print("入力された値は無効な値です")
