@--------------------
@ Data section
@--------------------
	.data
	.balign 4
Intro:	.asciz "Camera standby"
ErrMsg: .asciz "Setup didn’t work... Aborting...\n"
pin: 	.int 8
i: 	.int 0
OUTPUT = 1

@--------------------
@ Code section
@--------------------
	.text
	.global main
	.extern printf
	.extern wiringPiSetup
	.extern delay
	.extern digitalWrite
	.extern pinMode
main: PUSH {ip, lr} @ push return address + dummy register
					@ for alignment
@ printf( "blink..." ) ;
	LDR R0, =Intro
	BL printf
	
@ if (wiringPiSetup() == -1) {
@ printf( "Setup didn’t work... Aborting." ) ;
@ exit (1) ;
@ }
	BL wiringPiSetup
	MOV R1,#-1
	CMP R0, R1
	BNE init
	LDR R0, =ErrMsg
	BL printf
	B done

@ pinMode(pin, OUTPUT) ;
init:
	LDR R0, =pin
	LDR R0, [R0]
	MOV R1, #OUTPUT
	BL pinMode
	
@ digitalWrite(pin, 1) ;
	LDR R0, =pin
	LDR R0, [R0]
	MOV R1, #1
	BL digitalWrite

done:
	POP {ip, pc} @ pop return address into pc