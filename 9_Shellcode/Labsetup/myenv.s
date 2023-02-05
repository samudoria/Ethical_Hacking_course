section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string

      push "/env"
      push "/bin"
      push "/usr"
      mov  ebx, esp     ; Get the string address
      
      xor eax, eax
      push eax
      mov edx, esp

    ; Construct the argument array argv[]
      xor eax, eax
	    push eax          
      push edx
      push ecx
      push ebx          ; argv[0] points "/usr/bin/env"
      mov  ecx, esp     ; Get the address of argv[]
   
    ; For environment variable 
      mov eax, "4###"
	    shl eax, 24
	    shr eax, 24
      push eax
      push "=123"
      push "cccc"
	    mov edi, esp

      xor  eax, eax
      push eax
      push "5678"
      push "bbb="
      mov esi, esp

	    xor  eax, eax
      push eax
      push "1234"
      push "aaa="
      mov edx, esp

      push eax
	    push edi
	    push esi
	    push edx
	    mov  edx, esp     ; Get the address of environment variables
      
	  ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
