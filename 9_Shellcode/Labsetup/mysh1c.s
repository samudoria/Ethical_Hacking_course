section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string
	  push "//sh"
	  push "/bin"
      mov  ebx, esp     ; Get the string address

	  xor eax, eax
	  mov eax, "-c##"
	  shl eax, 16
	  shr eax, 16
	  push eax
	  mov ecx, esp

	  xor eax, eax
	  mov eax, "la##"
	  shl eax, 16
	  shr eax, 16
	  push eax
	  push "ls -"
	  mov edx, esp

      ; Construct the argument array argv[]
	  xor eax, eax
      push eax          ; argv[3] = 0
	  push edx          ; argv[2] => "ls -la"
	  push ecx          ; argv[1] => "-c"
      push ebx          ; argv[0] => "/bin/bash"
      mov  ecx, esp     ; Get the address of argv[]
   
      ; For environment variable 
      xor  edx, edx     ; No env variables 

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
