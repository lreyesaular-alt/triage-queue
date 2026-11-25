import unittest
from triage_queue import Patient, TriageQueue


class TestTriageQueue(unittest.TestCase):

    def setUp(self):
        self.queue = TriageQueue()

    def test_priority_order(self):
        self.queue.enqueue(Patient("Carlos", 3))
        self.queue.enqueue(Patient("Maria", 2))
        self.queue.enqueue(Patient("Pedro", 1))
        self.queue.enqueue(Patient("Ana", 2))

        names = [p.name for p in self.queue.list_queue()]
        self.assertEqual(
            names, ["Pedro", "Maria", "Ana", "Carlos"]
        )

    def test_fifo(self):
        self.queue.enqueue(Patient("Maria", 2))
        self.queue.enqueue(Patient("Ana", 2))

        self.assertEqual(self.queue.dequeue().name, "Maria")
        self.assertEqual(self.queue.dequeue().name, "Ana")

    def test_peek(self):
        self.queue.enqueue(Patient("Pedro", 1))

        self.assertEqual(self.queue.peek().name, "Pedro")
        self.assertEqual(len(self.queue.list_queue()), 1)

    def test_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_stats(self):
        self.queue.enqueue(Patient("Pedro", 1))
        self.queue.enqueue(Patient("Maria", 2))

        self.assertEqual(
            self.queue.stats(), {1: 1, 2: 1, 3: 0}
        )

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Patient("Carlos", 5)


if __name__ == "__main__":
    unittest.main()