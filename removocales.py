class Solution:
    def removeVowels(self, S: str) -> str:
        vowels ='aeiou'
        respuesta= []
        
        
        #Se realiza el proceso con for para tomar la letra de una sola vez
        for i in S:
            #Se hace comparacion con las letras guardadas previamente
            if i not in vowels:
                respuesta.append(i)
            
            i=+1
        
        #Se agregaran todas las respuesta con el join...para que sea un string
        return "".join(respuesta)
