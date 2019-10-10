from model.unsupervised import unspupervised


if __name__ == "__main__":
    str1 = "the cat is on the mat"
    str2 = "there is a cat on mat"
    print(unspupervised(str1, str2))
