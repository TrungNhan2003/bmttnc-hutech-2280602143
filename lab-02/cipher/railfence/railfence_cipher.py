class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        # Reconstruct the ciphertext
        ciphertext = ""
        for rail in rails:
            ciphertext += "".join(rail)
        return ciphertext

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Create a matrix to simulate the rail fence
        matrix = [['\n'] * len(cipher_text) for _ in range(num_rails)]

        # Mark the positions where characters would be placed
        rail_index = 0
        direction = 1
        col = 0
        for _ in range(len(cipher_text)):
            matrix[rail_index][col] = '*'
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            col += 1

        # Fill the matrix with the ciphertext
        index = 0
        for r in range(num_rails):
            for c in range(len(cipher_text)):
                if matrix[r][c] == '*':
                    matrix[r][c] = cipher_text[index]
                    index += 1

        # Read the plaintext from the matrix
        plain_text = ""
        rail_index = 0
        direction = 1
        col = 0
        for _ in range(len(cipher_text)):
            plain_text += matrix[rail_index][col]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            col += 1
        return plain_text