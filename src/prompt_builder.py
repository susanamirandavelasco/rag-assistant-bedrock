"""
Versión 1 del System Prompt.

Objetivos:
- Grounding
- Respuestas orientadas a negocio
- Máximo 100 palabras
- No responder fuera del contexto
"""

from src.models.models import RetrievedChunk, RetrievalResult

SYSTEM_PROMPT = """
Eres un experto en soluciones de Inteligencia Artificial de AWS.

Se te proporcionará información extraída de la documentación oficial de Amazon Bedrock.

Instrucciones:

- Utiliza únicamente el contexto proporcionado.
- Si la respuesta no se encuentra en el contexto, responde exactamente:
  "No encontré suficiente información en la documentación proporcionada para responder esa pregunta."
- No inventes información.
- Explica los conceptos de forma clara y orientada a negocio.
- Evita tecnicismos innecesarios.
- Limita la respuesta a un máximo de 100 palabras.
"""

class PromptBuilder:

    def build_prompt(
        self,
        query: str,
        retrieval_result: RetrievalResult
    ) -> str:

        context = ""

        for i, chunk in enumerate(retrieval_result.chunks, start=1):

            context += (
                f"Contexto {i}:\n"
                f"{chunk.content}\n\n"
            )

            """
            en algún momento reemplazaremos la línea anterior por la siguiente línea
            context = "\n\n".join(...)
            """

        prompt = f"""
            {SYSTEM_PROMPT}

            Contexto recuperado de la documentación oficial:

            {context}

            Pregunta:

            {query}

            Respuesta:
            """

        return prompt