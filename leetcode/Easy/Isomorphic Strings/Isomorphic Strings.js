/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  if (s.length !== t.length) return false;

  const mapping = {};
  const used = new Set();

  for (let i = 0; i < s.length; i++) {
    if (mapping.hasOwnProperty(t[i])) {
      if (mapping[t[i]] !== s[i]) {
        return false;
      }
    } else {
      if (used.has(s[i])) {
        return false;
      }
      mapping[t[i]] = s[i];
      used.add(s[i]);
    }
  }

  return true;
};

console.log(isIsomorphic("eggg", "addc"));
