import glob
import Junk_Voice_Mail


def classify_glob_path(path):
    results = dict()
    totals = dict()
    totals["total"] = 0
    totals["true"] = 0
    totals["none"] = 0
    totals["false"] = 0
    
    for fname in glob.glob(path):
        with open(fname) as file_handle:
            text = file_handle.read()
            output = Junk_Voice_Mail.DecSpam(text)
            print(fname, output)
            results[fname] = output
            totals["total"] += 1

    for fname, result in results.items():
        lowered = str(result).lower()
        totals[lowered] += 1

    return totals


def do_all_tests():
    Junk_Voice_Mail.DEBUGGING = False

    spam_path = "data/spam-train/spmsga*.txt"
    nonspam_path = "data/nonspam-train/*.txt"

    print("=====\nDecSpam result for Spam training data:")
    spam_totals = classify_glob_path(spam_path)
    print(spam_totals)
    print({k:x/spam_totals["total"] for k,x in spam_totals.items()})
    print("=====\nDecSpam results for Non-Spam training data:")
    nonspam_totals = classify_glob_path(nonspam_path)
    print(nonspam_totals)
    print({k:x/nonspam_totals["total"] for k,x in nonspam_totals.items()})
    print("\n[true means it is considered spam, none means it couldn't classify it.]")


spam_path = "data/spam-train/spmsga[1-9].txt"
print(classify_glob_path(spam_path))
