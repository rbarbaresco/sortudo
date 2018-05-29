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
    #IO.puts elements
    #insertion_sort(rest)
    for index <- 1..length(elements) do
      current = Enum.at(elements, index)
      IO.puts current
    end

    #for {el, index} <- Enum.with_index(elements) do
    #  position = index + 1
    #
    #end
  end
  def insertion_sort(current, x) do
    IO.puts current
  end
end
