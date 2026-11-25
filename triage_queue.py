from dataclasses import dataclass, field
from datetime import datetime
from collections import deque


@dataclass
class Patient:
    name: str
    triage_level: int
    arrived_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if self.triage_level not in (1, 2, 3):
            raise ValueError("El nivel de triaje debe ser 1, 2 o 3.")


class TriageQueue:
    def __init__(self):
        self.queues = {
            1: deque(),
            2: deque(),
            3: deque()
        }

    def enqueue(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Debe proporcionar un paciente válido.")
        self.queues[patient.triage_level].append(patient)

    def dequeue(self):
        for level in (1, 2, 3):
            if self.queues[level]:
                return self.queues[level].popleft()
        raise IndexError("No hay pacientes en espera.")

    def peek(self):
        for level in (1, 2, 3):
            if self.queues[level]:
                return self.queues[level][0]
        raise IndexError("No hay pacientes en espera.")

    def list_queue(self):
        return [
            patient
            for level in (1, 2, 3)
            for patient in self.queues[level]
        ]

    def stats(self):
        return {
            level: len(self.queues[level])
            for level in (1, 2, 3)
        }


def show_patient(patient):
    time = patient.arrived_at.strftime("%H:%M:%S")
    print(
        f"Nombre: {patient.name} | "
        f"Nivel: {patient.triage_level} | "
        f"Llegada: {time}"
    )


def main():
    queue = TriageQueue()

    while True:
        print("\n===== TRIAGE QUEUE =====")
        print("1. Añadir paciente")
        print("2. Llamar al siguiente paciente")
        print("3. Ver cola actual")
        print("4. Ver estadísticas")
        print("5. Ver siguiente paciente")
        print("6. Salir")

        option = input("\nSelecciona una opción: ").strip()

        if option == "1":
            name = input("Nombre del paciente: ").strip()

            try:
                level = int(input("Nivel de triaje (1-3): "))
                patient = Patient(name, level)
                queue.enqueue(patient)
                print("Paciente añadido correctamente.")
            except ValueError as error:
                print(f"Error: {error}")

        elif option == "2":
            try:
                patient = queue.dequeue()
                print("\nPaciente llamado:")
                show_patient(patient)
            except IndexError as error:
                print(f"Error: {error}")

        elif option == "3":
            patients = queue.list_queue()

            if not patients:
                print("No hay pacientes en espera.")
            else:
                print("\nPacientes en orden de atención:")
                for position, patient in enumerate(patients, 1):
                    print(f"{position}. ", end="")
                    show_patient(patient)

        elif option == "4":
            statistics = queue.stats()
            print("\nEstadísticas:")
            for level, count in statistics.items():
                print(f"Nivel {level}: {count} pacientes")
            print(f"Total: {sum(statistics.values())}")

        elif option == "5":
            try:
                print("\nSiguiente paciente:")
                show_patient(queue.peek())
            except IndexError as error:
                print(f"Error: {error}")

        elif option == "6":
            print("Cerrando Triage Queue. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()