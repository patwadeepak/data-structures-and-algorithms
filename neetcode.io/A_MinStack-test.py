from A_MinStack import MinStack1, MinStack2, MinStack3

class TestMinStack():
    def test_min_stack_dynamic(self, MinStack, inputs, expected_outputs):
        outputs = []

        stack = None
        for i in range(len(inputs)):
            input = inputs[i]
            if input == "MinStack":
                stack = MinStack()
                outputs.append(None)
            elif input == "push":
                stack.push(inputs[i + 1])
                outputs.append(None)
            elif input == "pop":
                stack.pop()
                outputs.append(None)
            elif input == "top":
                outputs.append(stack.top())
            elif input == "getMin":
                outputs.append(stack.getMin())

        if expected_outputs:
            self.assertEqual(outputs, expected_outputs)
        else:
            print(outputs)
        

if __name__ == "__main__":
    a = TestMinStack()

    inputs = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
    outputs = [None, None, None, None, 0, None, 2, 0]

    # solution 1
    a.test_min_stack_dynamic(MinStack1, inputs, outputs)
    # solution 2
    a.test_min_stack_dynamic(MinStack2, inputs, outputs)
    # solution 3
    a.test_min_stack_dynamic(MinStack3, inputs, outputs)
