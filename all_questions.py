# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {"smoking": 1,
             "smoking_info_gain": 0.2780719,
             "cough": -1,
             "cough_info_gain": -1,
             "radon": -1,
             "radon_info_gain": -1,
             "weight_loss": -1,
             "weight_loss_info_gain": -1,
             }
    level2_left = {"smoking": -1,
                "smoking_info_gain": -1,
                "cough": 1,
                "cough_info_gain": 0.03485155,
                "radon": -1,
                "radon_info_gain": -1,
                "weight_loss": -1,
                "weight_loss_info_gain": -1,
                }
    
    level2_right = {"smoking": -1,
                    "smoking_info_gain": -1,
                    "cough": -1,
                    "cough_info_gain": -1,
                    "radon": 1,
                    "radon_info_gain": 0.23645279,
                    "weight_loss": -1,
                    "weight_loss_info_gain": -1,
                   }

    level1["smoking"] = 1.
    level1["smoking_info_gain"] = 0.2780719

    level1["cough"] = -1.
    level1["cough_info_gain"] = -1.

    level1["radon"] = -1.
    level1["radon_info_gain"] = -1.

    level1["weight_loss"] = -1.
    level1["weight_loss_info_gain"] = -1.

    level2_left["smoking"] = -1.
    level2_left["smoking_info_gain"] = -1.
    level2_right["smoking"] = -1.
    level2_right["smoking_info_gain"] = -1.

    level2_left["radon"] = -1.
    level2_left["radon_info_gain"] = -1.

    level2_left["cough"] = 1.
    level2_left["cough_info_gain"] = 0.03485155

    level2_left["weight_loss"] = -1.
    level2_left["weight_loss_info_gain"] = -1.

    level2_right["radon"] = 1.
    level2_right["radon_info_gain"] = 0.23645279

    level2_right["cough"] = -1.
    level2_right["cough_info_gain"] = -1.

    level2_right["weight_loss"] = -1.
    level2_right["weight_loss_info_gain"] = -1.

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    #tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****

    tree = u.BinaryTree("smoking")
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    A.insert_left("yes")
    A.insert_right("no")
    B.insert_left("yes")
    B.insert_right("no")
    
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0

    

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.425364
    # Infogain
    answer["(b) x <= 0.2"] = 0.5637042
    answer["(b) x <= 0.7"] = 0.3022116
    answer["(b) y <= 0.6"] = 0.385102388

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = 'x=0.2'

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("x <= 0.2")
    A = tree.insert_left("y <= 0.6")
    B = tree.insert_right("x <= 0.7")
    A1 = A.insert_left("y <= 0.3")
    A2 = A.insert_right("y <= 0.8")
    B1 = B.insert_left("y <= 0.6")
    B2 = B.insert_right("y <= 0.3")
    A1.insert_left("C")
    A1.insert_right("B")
    A2.insert_left("B")
    A2.insert_right("C")
    B1.insert_left("A")
    B1.insert_right("C")
    B2.insert_left("C")
    B2.insert_right("A")

    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.0

    # float
    answer["(b) Gini, ID"] = 0.95
    answer["(c) Gini, Gender"] = 0.5
    answer["(d) Gini, Car type"] = 0.639999
    answer["(e) Gini, Shirt type"] = 0.

    answer["(f) attr for splitting"] = "Gender"

    # Explanatory text string
    answer["(f) explain choice"] = "its Gini index is high, indicating maximum impurity for a binary attribute, it's lower than the Gini index for Car Type, suggesting it might lead to more homogenous subsets. Additionally, since Gender is a binary attribute, it simplifies the initial split and can often lead to a more balanced tree structure."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary', 'qualitative', 'nominal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = ""

    answer["b"] = ['continuous', 'quantitative', 'ratio']
    answer["b: explain"] = ""

    answer["c"] = ['discrete', 'qualittive', 'ordinal']
    answer["c: explain"] = "There could be some ambiguity. For instance, if people rate brightness on a numerical scale (like 1 to 10), it could be argued that it's quantitative (as it uses numbers)"

    answer["d"] = ['continuous', 'quantitative', 'interval']
    answer["d: explain"] = "Angles should be considered as interval or ratio. Some might argue for ratio since 0 degrees can be seen as the absence of an angle."

    answer["e"] = ['discrete', 'qualitative', 'ordinal']
    answer["e: explain"] = ""

    answer["f"] = ['continuous', 'quantitative', 'ratio']
    answer["f: explain"] = ""

    answer["g"] = ['discrete', 'quantitative', 'ratio']
    answer["g: explain"] = ""

    answer["h"] = ['discrete', 'qualitative', 'nominal']
    answer["h: explain"] = ""

    answer["i"] = ['discrete', 'qualitative', 'ordinal']
    answer["i: explain"] = ""

    answer["j"] = ['discrete', 'qualitative', 'ordinal']
    answer["j: explain"] = ""

    answer["k"] = ['continuous', 'quantitative', 'ratio']
    answer["k: explain"] = ""

    answer["l"] = ['continuous', 'quantitative', 'ratio']
    answer["l: explain"] = ""

    answer["m"] = ['discrete', 'qualitative', 'nominal']
    answer["m: explain"] = ""

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Has a lower accuracy on the training set but its accuracy on the testing set is quite close to its training accuracy. This suggests that the model has a better balance between bias and variance, meaning it's less overfit to the training data and is likely to generalize better to unseen data."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Model 2 might still be preferable despite its slightly lower overall accuracy, because it's less likely to suffer from overfitting and may perform better with completely unseen data in the future."

    explain["c similarity"] = "Penalizing Complexity"
    explain["c similarity explain"] = "They both aim to avoid overly complex trees that fit the noise in the training data, rather than the underlying distribution. They both effectively add a regularization term to the loss function that increases with the complexity of the tree."

    explain["c difference"] = "Method of Penalization"
    explain["c difference explain"] = "MDL is based on information theory and seeks to minimize the combined cost of the model and the data given the model. In decision trees, this often translates to preferring smaller trees as they typically require fewer bits to describe than larger trees. Pessimistic Error Estimate adjusts the error rate of a tree on the training data by adding a penalty that increases with the number of leaves in the tree."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1
    answer["b, info gain, Handedness"] =  0.531004

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.231378
    answer["e, gain ratio, Handedness"] = 0.531004

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)
