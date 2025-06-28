"""
CLARIFICATION QUESTIONS PATTERN - Progressive Information Gathering

This pattern demonstrates how to create tools that intelligently ask for missing
information before proceeding. Instead of failing when parameters are missing,
the tool guides users through providing the necessary details step by step.

Key features of this pattern:
1. 🤔 SMART DETECTION: Identifies what information is missing
2. 📝 PROGRESSIVE GATHERING: Builds up information across multiple calls
3. 🎯 CONTEXTUAL QUESTIONS: Asks relevant questions based on what's known
4. 💾 SESSION MEMORY: Remembers partial information between interactions
5. ✅ COMPLETION DETECTION: Only proceeds when all required info is available

This is perfect for complex tools where users might not know all parameters upfront,
or where the tool needs to guide users through a decision-making process.
"""

from typing import Dict, Any, Optional
from fastmcp import FastMCP

# Session storage for clarification-based tools
_recipe_sessions: Dict[str, Dict[str, Any]] = {}

def register_clarification_questions_tools(mcp: FastMCP):
    """Register clarification questions pattern tools with the MCP server"""
    
    @mcp.tool
    def smart_recipe_generator(
        session_id: str = "default",
        user_response: Optional[str] = None,
        cuisine_type: Optional[str] = None,
        dietary_restrictions: Optional[str] = None, 
        cooking_time: Optional[str] = None,
        skill_level: Optional[str] = None,
        meal_type: Optional[str] = None,
        serving_size: Optional[str] = None,
        ingredients_preference: Optional[str] = None
    ) -> str:
        """
        CLARIFICATION QUESTIONS PATTERN EXAMPLE: A smart recipe generator that asks clarifying questions.
        
        This tool demonstrates the "Progressive Information Gathering" pattern where the tool
        intelligently identifies missing information and asks targeted clarification questions
        instead of failing. It builds up a complete recipe specification across multiple calls.
        
        🍳 EXAMPLE USAGE FLOW:
        1. User: "Generate a recipe" (no parameters)
        2. Tool: "Ask the user: What cuisine type would you like?"
        3. AI: Asks user the question and waits for response
        4. User: Responds "Italian"
        5. AI: Calls with user_response="Italian"
        6. Tool: "Ask the user: Any dietary restrictions?"
        7. ...continues until all required info is gathered
        8. Tool: Generates complete personalized recipe
        
        Args:
            session_id: Unique identifier to track this recipe session (defaults to "default")
            user_response: The user's actual response to the previous question (REQUIRED for follow-ups)
            cuisine_type: Type of cuisine (Italian, Asian, Mexican, etc.)
            dietary_restrictions: Any dietary needs (vegetarian, vegan, gluten-free, etc.)
            cooking_time: Available cooking time (quick-15min, standard-45min, elaborate-1hr+)
            skill_level: Cooking expertise (beginner, intermediate, advanced)
            meal_type: What meal (breakfast, lunch, dinner, snack, dessert)
            serving_size: How many people (1-2, 3-4, 5-6, large-group)
            ingredients_preference: Specific ingredients to include/avoid (optional)
        
        Returns:
            Either a clarification question for missing info, or a complete recipe when ready
        """
        # Initialize or retrieve session data
        if session_id not in _recipe_sessions:
            _recipe_sessions[session_id] = {}
        
        session = _recipe_sessions[session_id]
        
        # Process user response if provided
        if user_response and user_response.strip():
            # Determine which field to update based on current session state
            if 'cuisine_type' not in session:
                session['cuisine_type'] = user_response.strip()
            elif 'dietary_restrictions' not in session:
                session['dietary_restrictions'] = user_response.strip()
            elif 'cooking_time' not in session:
                session['cooking_time'] = user_response.strip()
            elif 'skill_level' not in session:
                session['skill_level'] = user_response.strip()
            elif 'meal_type' not in session:
                session['meal_type'] = user_response.strip()
            elif 'serving_size' not in session:
                session['serving_size'] = user_response.strip()
        
        # Also update session with any directly provided parameters (for flexibility)
        if cuisine_type:
            session['cuisine_type'] = cuisine_type
        if dietary_restrictions:
            session['dietary_restrictions'] = dietary_restrictions
        if cooking_time:
            session['cooking_time'] = cooking_time
        if skill_level:
            session['skill_level'] = skill_level
        if meal_type:
            session['meal_type'] = meal_type
        if serving_size:
            session['serving_size'] = serving_size
        if ingredients_preference:
            session['ingredients_preference'] = ingredients_preference
        
        # Check what information is still missing and ask clarification questions
        if 'cuisine_type' not in session:
            return f"""🚨 **STOP - ASK THE USER** 🚨

❌ **DO NOT MAKE ASSUMPTIONS OR GUESS**
✅ **YOU MUST ASK THE USER THIS QUESTION:**

"What type of cuisine would you like to explore?"

**Options to mention:**
• 🇮🇹 Italian (pasta, pizza, risotto)
• 🇨🇳 Asian (Chinese, Thai, Japanese, Korean)  
• 🇲🇽 Mexican (tacos, burritos, enchiladas)
• 🇺🇸 American (BBQ, comfort food, burgers)
• 🇬🇷 Mediterranean (Greek, Turkish, Middle Eastern)
• 🇮🇳 Indian (curry, tandoori, biryani)
• 🇫🇷 French (classic techniques, sauces)

⚠️ **IMPORTANT**: After the user replies, call this tool again with user_response="[their exact answer]"

📊 **Progress:** 1/6 questions needed
🔄 **Next:** Wait for user input, then call with user_response parameter"""

        if 'dietary_restrictions' not in session:
            return f"""🚨 **STOP - ASK THE USER** 🚨

❌ **DO NOT MAKE ASSUMPTIONS OR GUESS**
✅ **YOU MUST ASK THE USER THIS QUESTION:**

"Do you have any dietary restrictions or preferences?"

**Options to mention:**
• ✅ None (no restrictions)
• 🥬 Vegetarian (no meat)
• 🌱 Vegan (no animal products)
• 🌾 Gluten-free (no wheat/gluten)
• 🥛 Dairy-free (no milk products)
• 🥜 Nut-free (allergy considerations)
• 🥩 Keto (low-carb, high-fat)
• ❤️ Heart-healthy (low sodium, low fat)

⚠️ **IMPORTANT**: After the user replies, call this tool again with user_response="[their exact answer]"

📊 **Progress:** 2/6 questions needed
✅ **Cuisine chosen:** {session.get('cuisine_type')}
🔄 **Next:** Wait for user input, then call with user_response parameter"""

        if 'cooking_time' not in session:  
            return f"""🚨 **STOP - ASK THE USER** 🚨

❌ **DO NOT MAKE ASSUMPTIONS OR GUESS**  
✅ **YOU MUST ASK THE USER THIS QUESTION:**

"How much time do you have available for cooking?"

**Options to mention:**
• ⚡ Quick (15-20 minutes) - Simple, fast meals
• 🍳 Standard (30-45 minutes) - Most home cooking  
• 👨‍🍳 Elaborate (1+ hours) - Complex, impressive dishes
• 🔄 Variable - I have flexible time

⚠️ **IMPORTANT**: After the user replies, call this tool again with user_response="[their exact answer]"

📊 **Progress:** 3/6 questions needed
✅ **Chosen so far:** {session.get('cuisine_type')} | {session.get('dietary_restrictions')}
🔄 **Next:** Wait for user input, then call with user_response parameter"""

        if 'skill_level' not in session:
            return f"""🚨 **STOP - ASK THE USER** 🚨

❌ **DO NOT MAKE ASSUMPTIONS OR GUESS**
✅ **YOU MUST ASK THE USER THIS QUESTION:**

"What's your cooking experience level?"

**Options to mention:**
• 🔰 Beginner - Simple recipes, basic techniques
• 🍳 Intermediate - Comfortable with most techniques  
• 👨‍🍳 Advanced - Complex techniques, confident with flavors
• 🎓 Expert - Professional-level skills

⚠️ **IMPORTANT**: After the user replies, call this tool again with user_response="[their exact answer]"

📊 **Progress:** 4/6 questions needed
✅ **Profile so far:** {session.get('cuisine_type')} | {session.get('dietary_restrictions')} | {session.get('cooking_time')}
🔄 **Next:** Wait for user input, then call with user_response parameter"""

        if 'meal_type' not in session:
            return f"""🚨 **STOP - ASK THE USER** 🚨

❌ **DO NOT MAKE ASSUMPTIONS OR GUESS**
✅ **YOU MUST ASK THE USER THIS QUESTION:**

"What type of meal are you planning?"

**Options to mention:**
• 🌅 Breakfast - Start the day right
• 🥪 Lunch - Midday fuel
• 🍽️ Dinner - Main evening meal
• 🍿 Snack - Light bite
• 🍰 Dessert - Sweet finish
• 🥗 Appetizer - Party starter

⚠️ **IMPORTANT**: After the user replies, call this tool again with user_response="[their exact answer]"

📊 **Progress:** 5/6 questions needed
✅ **Profile so far:** {session.get('cuisine_type')} | {session.get('dietary_restrictions')} | {session.get('cooking_time')} | {session.get('skill_level')}
🔄 **Next:** Wait for user input, then call with user_response parameter"""

        if 'serving_size' not in session:
            return f"""🚨 **STOP - ASK THE USER** 🚨

❌ **DO NOT MAKE ASSUMPTIONS OR GUESS**
✅ **YOU MUST ASK THE USER THIS QUESTION:**

"How many people will you be cooking for?"

**Options to mention:**
• 👤 Solo (1 person) - Just for me
• 💑 Couple (2 people) - Intimate meal
• 👨‍👩‍👧 Small family (3-4 people) - Family dinner
• 👥 Large family (5-6 people) - Big household  
• 🎉 Group (7+ people) - Party or gathering

⚠️ **IMPORTANT**: After the user replies, call this tool again with user_response="[their exact answer]"

📊 **Progress:** 6/6 questions needed (FINAL QUESTION!)
✅ **Profile so far:** {session.get('cuisine_type')} | {session.get('dietary_restrictions')} | {session.get('cooking_time')} | {session.get('skill_level')} | {session.get('meal_type')}
🔄 **Next:** Wait for user input, then call with user_response parameter"""

        # All required information collected! Generate the recipe
        profile = session
        
        # Generate a personalized recipe based on collected preferences
        recipe_title = f"{profile['cuisine_type']} {profile['meal_type'].title()}"
        if profile['dietary_restrictions'] != 'None':
            recipe_title += f" ({profile['dietary_restrictions']})"
        
        # Create recipe based on preferences
        difficulty_emoji = {"beginner": "🔰", "intermediate": "🍳", "advanced": "👨‍🍳", "expert": "🎓"}
        time_emoji = {"quick-15min": "⚡", "standard-45min": "🍳", "elaborate-1hr+": "👨‍🍳", "variable": "🔄"}
        
        recipe = f"""🎉 **RECIPE GENERATED SUCCESSFULLY!**

# {recipe_title}
{difficulty_emoji.get(profile['skill_level'], '🍳')} **Difficulty:** {profile['skill_level'].title()}
{time_emoji.get(profile['cooking_time'], '⏰')} **Time:** {profile['cooking_time'].replace('-', ' to ').replace('+', ' or more')}
👥 **Serves:** {profile['serving_size'].replace('-', ' to ')}

## 🛒 **Ingredients:**
{_generate_ingredients(profile)}

## 📝 **Instructions:**
{_generate_instructions(profile)}

## 💡 **Chef's Tips:**
{_generate_tips(profile)}

---
✅ **CLARIFICATION PATTERN SUCCESS!** 
All 6 questions answered through progressive information gathering.

**Your Complete Profile:**
{' | '.join([f"{k}: {v}" for k, v in profile.items()])}

🗑️ Session data cleared. Start fresh anytime with a new session_id!"""

        # Clear the session after successful recipe generation
        del _recipe_sessions[session_id]
        
        return recipe


def _generate_ingredients(profile: Dict[str, str]) -> str:
    """Generate ingredients list based on user profile"""
    base_ingredients = {
        'Italian': ['• 400g pasta or rice', '• 2 cloves garlic', '• 2 tbsp olive oil', '• Fresh basil', '• Parmesan cheese'],
        'Asian': ['• 2 cups rice or noodles', '• 2 tbsp soy sauce', '• 1 tbsp sesame oil', '• Fresh ginger', '• Green onions'],
        'Mexican': ['• Tortillas or rice', '• Black beans', '• Tomatoes', '• Cilantro', '• Lime', '• Avocado'],
        'American': ['• 1 lb protein of choice', '• Potatoes', '• Onions', '• Butter', '• Salt & pepper'],
        'Mediterranean': ['• Olive oil', '• Tomatoes', '• Feta cheese', '• Olives', '• Fresh herbs'],
        'Indian': ['• Basmati rice', '• Curry powder', '• Coconut milk', '• Onions', '• Garlic & ginger'],
        'French': ['• Butter', '• Shallots', '• White wine', '• Fresh herbs', '• Cream']
    }
    
    ingredients = base_ingredients.get(profile['cuisine_type'], base_ingredients['American'])
    
    # Modify based on dietary restrictions
    if 'vegan' in profile.get('dietary_restrictions', '').lower():
        ingredients = [ing.replace('cheese', 'nutritional yeast').replace('butter', 'vegan butter').replace('cream', 'coconut cream') for ing in ingredients]
    elif 'vegetarian' in profile.get('dietary_restrictions', '').lower():
        ingredients = [ing for ing in ingredients if 'meat' not in ing.lower()]
    
    return '\n'.join(ingredients)


def _generate_instructions(profile: Dict[str, str]) -> str:
    """Generate cooking instructions based on user profile"""
    if profile['skill_level'] == 'beginner':
        return """1. 🔥 Heat oil in a large pan over medium heat
2. 🧄 Add garlic and cook for 1 minute until fragrant  
3. 🥘 Add main ingredients and cook according to package directions
4. 🧂 Season with salt and pepper to taste
5. 🍽️ Serve hot and enjoy!

*Simple and straightforward - perfect for beginners!*"""
    elif profile['skill_level'] == 'advanced':
        return """1. 🔥 Create a flavor base with aromatics using proper mise en place
2. 🎯 Build layers of flavor through careful timing and temperature control
3. 🧪 Balance acidity, sweetness, and umami for optimal taste profile
4. 🎨 Focus on presentation and garnish for visual appeal
5. 🍷 Consider wine pairing suggestions for elevated dining experience

*Advanced techniques for the experienced home chef*"""
    else:
        return """1. 🔥 Prepare all ingredients before starting (mise en place)
2. 🥘 Cook in stages, building flavors step by step
3. 👅 Taste and adjust seasoning throughout cooking
4. ⏰ Pay attention to timing for best results
5. 🎨 Plate thoughtfully and serve immediately

*Balanced approach for intermediate cooks*"""


def _generate_tips(profile: Dict[str, str]) -> str:
    """Generate cooking tips based on user profile"""
    tips = []
    
    if profile['cooking_time'] == 'quick-15min':
        tips.append("⚡ **Speed Tip:** Prep all ingredients before cooking starts")
    elif profile['cooking_time'] == 'elaborate-1hr+':
        tips.append("👨‍🍳 **Patience Tip:** Low and slow often yields the best flavors")
    
    if 'gluten-free' in profile.get('dietary_restrictions', ''):
        tips.append("🌾 **Gluten-Free:** Double-check all sauces and seasonings for hidden gluten")
    
    if profile['skill_level'] == 'beginner':
        tips.append("🔰 **Beginner Tip:** Don't be afraid to taste as you go - it's how you learn!")
    
    cuisine_tips = {
        'Italian': "🇮🇹 **Italian Secret:** Good olive oil makes all the difference",
        'Asian': "🇨🇳 **Asian Wisdom:** High heat and quick cooking preserves texture",
        'Mexican': "🇲🇽 **Mexican Magic:** Toast your spices for deeper flavor"
    }
    
    if profile['cuisine_type'] in cuisine_tips:
        tips.append(cuisine_tips[profile['cuisine_type']])
    
    return '\n'.join(tips) if tips else "🍳 **General Tip:** Cook with love and confidence!" 