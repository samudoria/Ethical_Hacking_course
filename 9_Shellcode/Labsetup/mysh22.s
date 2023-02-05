section .text
  global _start
    _start:
      BITS 32
      jmp short two

    one:
      pop ebx
      xor eax, eax
      mov [ebx+12], al
      push eax
      push eax
      push dword [ebx+13]
      push eax
      push dword [ebx+17]

      push eax
      lea esi, [esp+4]
      push esi
      lea esi, [esp+16]
      push esi
      mov edx, esp

      xor eax, eax
      mov al, 0x0b
      int 0x80

    two:
      call one
      db '/usr/bin/env*a=11b=22'
