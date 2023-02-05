section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string
      
	  ; task 1.1 hard way
	  ;mov eax, 0x69696968
	  ;shl eax, 24
	  ;shr eax, 24
	  ;push eax
	  ;xor eax, eax

	  ; task 1.1 easy way
	  ;mov eax, 0x68
	  ;push eax
	  ;xor eax, eax
	  
	  ;task 1.1 prof way
	  mov eax, "h###"
	  shl eax, 24
	  shr eax, 24
	  push eax
	  xor eax, eax
	  
	  push "/bas"
	  push "/bin"
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax          ; argv[1] = 0
      push ebx          ; argv[0] points "/bin/bash"
      mov  ecx, esp     ; Get the address of argv[]
   
      ; For environment variable 
      xor  edx, edx     ; No env variables 

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
