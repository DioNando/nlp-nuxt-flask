export const useElementStore = defineStore("elementStore", {
  state: () => ({}),
  actions: {
    capitalizeText(text: string): string {
      const mots = text.split(" ");
      const motsFormattes = mots.map(
        (mot) => mot.charAt(0).toUpperCase() + mot.slice(1)
      );
      motsFormattes.shift();
      const resultat = motsFormattes.join(" ");
      return resultat;
    },
  },
});
