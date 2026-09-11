# AI Use Notes

## Tool used

ChatGPT / Codex

## Questions asked

1. What does this error mean?
   `AttributeError: 'AirConditioner' object has no attribute 'fan'`
2. Why does assigning to `self.temperature` inside the temperature setter cause a `RecursionError`?
3. Why did using `self.__temperature` make the valid-temperature test fail?
4. Why should `is_energy_saving` be calculated from the current temperature?
5. Why does the temperature range check require `or` instead of `and`?
6. Why must the constructor use the temperature setter?
7. How can `cooler()` avoid reducing the temperature below the minimum?

## What I learned

- Attribute names must match exactly.
- A property setter must write to its backing attribute to avoid calling itself repeatedly.
- Validation must reject values below the minimum or above the maximum.
- Constructors should use validated setters instead of bypassing them.
- A derived property should be calculated from the object's current state.
- Boundary checks prevent methods from creating invalid state.

## Disclosure

AI explained the errors and also suggested specific code changes. I entered the changes and ran the checker myself.
