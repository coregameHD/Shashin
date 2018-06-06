@--------------------
@ Data section
@--------------------
	.data
	.balign 4
Intro:	.asciz "Camera blink"
ErrMsg: .asciz "Setup didn’t work... Aborting...\n"
pin: 	.int 8
i: 		.int 0
delayMs: .int 50
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
	
@ for ( i=0; i<3; i++ ) {
	LDR R4, =i
	LDR R4, [R4]
	MOV R5, #3
forLoop:
	CMP R4, R5
	BGT done
	
@ digitalWrite(pin, 1) ;
	LDR R0, =pin
	LDR R0, [R0]
	MOV R1, #1
	BL digitalWrite

@ delay(50) ;
	LDR R0, =delayMs
	LDR R0, [R0]
	BL delay
	
@ digitalWrite(pin, 0) ;
	LDR R0, =pin
	LDR R0, [R0]
	MOV R1, #0
	BL digitalWrite

@ delay(50) ;
	LDR R0, =delayMs
	LDR R0, [R0]
	BL delay
	ADD R4, #1
	B forLoop
done:
	POP {ip, pc} @ pop return address into pc