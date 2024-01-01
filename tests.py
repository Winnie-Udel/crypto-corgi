# Run and stop running tests.py to see the test passes

from bakery import assert_equal
from main import *

# Unit test for helper functions
assert_equal(convert_to_ascii("Hi!"), [72, 105, 33])
assert_equal(rotation(convert_to_ascii("Hi!"), 1), [73, 106, 34])
assert_equal(insert_tilde(convert_to_ascii("Hi!")), [72, 105, 33, 126])
assert_equal(encrypt_text("Dragons!", 10), "N|kqyx}+~")
assert_equal(remove_tilde([72, 105, 33, 126]), [72, 105, 33])
assert_equal(decrypt_text("N|kqyx}+~", 10), "Dragons!")
assert_equal(transform_ascii([33, 34], 1), [1, 17179869184])
assert_equal(sum_values([33, 34]), 67)
assert_equal(hash_text("Hello", 31, 1000000000), 590934605)

# Unit test for website pages
assert_equal(index(State(2, "", "", "", "")),
    Page(state=State(2, "", "", "", ""),
        content=[Image("http://tinyurl.com/3ct5zznh", 600, 120),
        LineBreak(),
        """
        Welcome! Need to encrypt or decrypt a message? Well, you came to the 
        right place!
        """,
        HorizontalRule(),
        Link("Encryption", encryption),
        "Encrypt messages based on the rotation amount.",
        BulletedList(["Input: Message",
                      "Output: Encrypted Message and Hash Value"]),
        HorizontalRule(),
        Link("Decryption", decryption),
        "Decrypt encrypted messages based on the rotation amount.",
        BulletedList(["Input: Encrypted Message and Hash Value",
                      "Output: Decrypted Message"]),
        HorizontalRule(),
        Button("Setting", setting)
        ]))

assert_equal(encryption(State(2, "", "", "", "")),
    Page(state=State(2, "", "", "", ""),
        content=[Header("Encryption", 3),
        "Rotation Amount: " + str(2),
        HorizontalRule(),
        "Please enter your desired message to be encrypted!",
        TextBox("user_message", ""),
        HorizontalRule(),
        Table([["Encrypted Message", "Hash Value"],
               ["", ""]]),
        HorizontalRule(),
        Button("Submit", update_encryption),
        Button("Return Home", index, float="right")
        ]))

# Scenerio: User enters "Dragons!" as their choice of message to be encrypted
assert_equal(update_encryption(State(10, "Dragons!", "", "", ""), "Dragons!"),
    Page(state=State(10, "Dragons!", "N|kqyx}+~", "826251914", ""),
        content=[Header("Encryption", 3),
        "Rotation Amount: " + str(10),
        HorizontalRule(),
        "Please enter your desired message to be encrypted!",
        TextBox("user_message", "Dragons!"),
        HorizontalRule(),
        Table([["Encrypted Message", "Hash Value"],
               ["N|kqyx}+~", "826251914"]]),
        HorizontalRule(),
        Button("Submit", update_encryption),
        Button("Return Home", index, float="right")
        ]))

assert_equal(decryption(State(2, "", "", "", "")),
    Page(state=State(2, "", "", "", ""),
        content=[Header("Decryption", 3),
        "Rotation Amount: " + str(2),
        HorizontalRule(),
        "Please enter your encrypted message to be decrypted!",
        TextBox("encrypted_message", ""),
        "Please enter the hash value to your encrypted message!",
        TextBox("hash_value", ""),
        HorizontalRule(),
        Table([["Decrypted Message"],
               [""]]),
        HorizontalRule(),
        Button("Submit", update_decryption),
        Button("Return Home", index, float="right")
        ]))

# Scenerio: User-inputted hash value matches the computed hash value
assert_equal(update_decryption(State(10, "", "N|kqyx}+~", "826251914", ""), "N|kqyx}+~", "826251914"),
    Page(state=State(10, "", "N|kqyx}+~", "826251914", "Dragons!"),
        content=[Header("Decryption", 3),
        "Rotation Amount: " + str(10),
        HorizontalRule(),
        "Please enter your encrypted message to be decrypted!",
        TextBox("encrypted_message", "N|kqyx}+~"),
        "Please enter the hash value to your encrypted message!",
        TextBox("hash_value", "826251914"),
        HorizontalRule(),
        Table([["Decrypted Message"],
               ["Dragons!"]]),
        HorizontalRule(),
        Button("Submit", update_decryption),
        Button("Return Home", index, float="right")
        ]))

# Scenerio: User-inputted hash value does not match the computed hash value
assert_equal(update_decryption(State(10, "", "N|kqyx}+~", "123", ""), "N|kqyx}+~", "123"),
    Page(state=State(10, "", "N|kqyx}+~", "123", ""),
        content=[Header("Error!", 3),
        HorizontalRule(),
        """
        There's been an error. User-inputted hash value does not match the computed 
        hash value. Please try again!
        """,
        HorizontalRule(),
        Button("Try Again!", decryption)
        ]))

assert_equal(setting(State(2, "", "", "", "")),
    Page(state=State(2, "", "", "", ""),
        content=[Header("Setting", 3),
        HorizontalRule(),
        "Set the rotation amount.",
        SelectBox("rotation_amount",
                  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                  str(2)),
        HorizontalRule(),
        Button("Return Home", update_setting, float="right")
        ]))

# Scenerio: When the user selects 10 as their rotation amount
assert_equal(update_setting(State(2, "", "", "", ""), "10"),
    Page(state=State(10, "", "", "", ""),
        content=[Image("http://tinyurl.com/3ct5zznh", 600, 120),
        LineBreak(),
        """
        Welcome! Need to encrypt or decrypt a message? Well, you came to the 
        right place!
        """,
        HorizontalRule(),
        Link("Encryption", encryption),
        "Encrypt messages based on the rotation amount.",
        BulletedList(["Input: Message",
                      "Output: Encrypted Message and Hash Value"]),
        HorizontalRule(),
        Link("Decryption", decryption),
        "Decrypt encrypted messages based on the rotation amount.",
        BulletedList(["Input: Encrypted Message and Hash Value",
                      "Output: Decrypted Message"]),
        HorizontalRule(),
        Button("Setting", setting)
        ]))