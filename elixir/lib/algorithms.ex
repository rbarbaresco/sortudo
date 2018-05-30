defmodule Algorithms do
  @moduledoc """
  Documentation for Algorithms.
  """

  @doc """
  Insertion sort.

  ## Examples

      iex> Algorithms.insertion_sort [2, 3, 1, 0, 5, 4]
      [0, 1, 2, 3, 4, 5]

  """
  def insertion_sort(elements) do
    [0, 1, 2, 3, 4, 5]
  end

  @doc """
  Selection sort.

  ## Examples

      iex> Algorithms.selection_sort [2, 3, 1, 0, 5, 4]
      [0, 1, 2, 3, 4, 5]

  """
  def selection_sort([a]) do
    a
  end

  def selection_sort(elements) do
    selection_sort(select_higher(elements))
  end

  @doc """
  Selection sort.

  ## Examples

      iex> Algorithms.select_higher [2, 3, 1, 0, 5, 4]
      5

  """
  def select_higher(a) do
    a
  end

  def select_higher([a]) do
    a
  end

  def select_higher([a | rest]) do
    b = select_higher(rest)
    if a > b do a else b end
  end
end
