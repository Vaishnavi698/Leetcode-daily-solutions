class ProductOfNumbers:
    def __init__(self):
        # Initialize with 1 to handle full-length product divisions cleanly
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the prefix array because any product including this 0 is 0
            self.prefix = [1]
        else:
            # Append the new running product
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k reaches past the last reset (where 0 occurred), the product is 0
        if k >= len(self.prefix):
            return 0
        # Divide total running product by the prefix product right before the last k elements
        return self.prefix[-1] // self.prefix[-1 - k]
