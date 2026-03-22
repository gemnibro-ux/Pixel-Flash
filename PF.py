from os import system

class VirtualMachine:
    def __init__(self):
        self.registers = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}
        self.pc = 0
        self.running = True
        self.output = ""
        self.remove_registers = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}

    def reset(self):
        self.registers = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}
        self.pc = 0
        self.running = True
        self.output = ""

    def execute(self, instructions):
        self.reset()
        lines = instructions.strip().split('\n')
        while self.running and self.pc < len(lines):
            instr = lines[self.pc].strip().split()
            if not instr:
                self.pc += 1
                continue
            cmd = instr[0].upper()
            args = instr[1:]

            try:
                if cmd == 'PASTE':
                    self.remove_registers = self.registers
                    reg, val = args
                    self.registers[reg] = val
                elif cmd == 'ADD':
                    self.remove_registers = self.registers
                    reg1, reg2 = args
                    self.registers[reg1] += self.registers[reg2]
                elif cmd == 'REG':
                    reg = args[0]
                    if reg in self.registers:
                        self.output += f"{reg} = {self.registers[reg]}\n"
                    elif reg == "__REGS":
                        for reg in self.registers:
                            self.output += f"{reg} = {self.registers[reg]}\n"
                    else:
                        self.output += f"Ошибка: нет регистра {reg}\n"
                elif cmd == 'MSG':
                    message = args[0]
                    self.output += f"{message}\n"
                    if message is None:
                        self.output += f"\n"
                elif cmd == "MAKE":
                    reg, val = args
                    self.registers[reg] = val
                elif cmd == "DEL":
                    reg = args[0]
                    del(self.registers[reg])
                elif cmd == "MOVE":
                    reg1, reg2 = args
                    self.registers[reg1] = self.registers[reg2]
                elif cmd == "REMOVE":
                    reg = args[0]
                    self.registers[reg] = self.remove_registers[reg]
                elif cmd == 'HALT':
                    self.running = False
                elif cmd == 'CLEAR':
                    reg = args[0]
                    if reg in self.registers:
                        self.registers[reg] = 0
                    elif reg == "__REGS":
                        for reg in self.registers:
                            self.registers[reg] = 0
                    else:
                        self.output += f"Ошибка: нет регистра {reg}\n"
                else:
                    self.output += f"Ошибка: неизвестная команда {cmd}\n"
            except Exception as e:
                self.output += f"Ошибка в строке {self.pc + 1}: {e}\n"
                if self.registers == {}:
                    self.output += f"Ошибка: нет регистров! Пересоздаются обычные регистры.\n"
                    self.registers = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0}
                elif len(self.registers) >= 200:
                    self.output += f"Ошибка: регистров очень много! Пожалуйста удалите несколько регистров.\n"
                self.running = False

            self.pc += 1
        return self.output, self.registers
