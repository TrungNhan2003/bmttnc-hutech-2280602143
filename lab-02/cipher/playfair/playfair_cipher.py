class PlayFairCipher:
    def __init__(self) -> None:
        # Note: Having two __init__ methods is unusual and the second one
        # will overwrite the first. It's best to have only one.
        # Assuming the intention was a single __init__ that does nothing,
        # or to remove the type hint if it's not needed.
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I") # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        
        # Xử lý các ký tự trùng lặp trong khóa, giữ nguyên thứ tự xuất hiện lần đầu
        processed_key = []
        for char in key:
            if char not in processed_key:
                processed_key.append(char)

        key_set = set(processed_key) # Tạo set từ khóa đã xử lý để tìm remaining_letters
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set
        ]
        
        matrix = processed_key # Bắt đầu ma trận với khóa đã xử lý các ký tự trùng lặp

        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break
        
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1 # Thêm dòng này để xử lý trường hợp không tìm thấy ký tự

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1: # Xử lý nếu số lượng ký tự lẻ
                pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % \
                                              5] + matrix[row2][(col2 + 1) \
                                                                % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % \
                                        5][col1] + matrix[(row2 + 1) % \
                                                         5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        decrypted_text1 = "" # This variable seems unused, consider removing if not needed.

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % \
                                               5] + matrix[row2][(col2 - 1) \
                                                                 % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % \
                                         5][col1] + matrix[(row2 - 1) % 5] \
                                                        [col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        banro = ""
        # Loại bỏ ký tự 'X' nếu nó là ký tự cuối cùng và là ký tự được thêm thêm vào
        for i in range(0, len(decrypted_text) - 2, 2): # Changed range to step by 2
            if decrypted_text[i] == decrypted_text[i+2]: # This logic might be problematic for 'X' removal
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + "" + decrypted_text[i+1] # This adds an empty string, effectively just concatenating

        # The logic for handling the last one or two characters needs careful review
        # to correctly remove padding 'X's without altering original 'X's.
        # This part of the decryption is often the most complex and depends on
        # the exact padding rules used during encryption.
        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2]
            banro += decrypted_text[-1]
        return banro
